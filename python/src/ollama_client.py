import requests
import json
import logging
import re

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url.rstrip("/")
        self.logger = logging.getLogger(__name__)
        self.session = requests.Session() 
        self.headers = {
            'User-Agent': 'OllamaClient/1.0',
            'Accept': 'application/json'
        }
    
    def call(self, model: str, prompt: str, system_prompt: str = None, 
             stream: bool = False, options: dict = None) -> str:
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": stream,
            "options": options or {}
        }
        
        if system_prompt:
            payload["system"] = system_prompt
        
        try:
            with self.session.post(
                url, 
                json=payload, 
                timeout=60, 
                stream=stream,
                headers=self.headers
            ) as response:
                
                response.raise_for_status()
                content_type = response.headers.get('Content-Type', '')
                if 'application/json' not in content_type and not stream:
                    raise ValueError(f"Resposta inesperada: {content_type}")
                
                if stream:
                    return self._handle_stream_response(response)
                else:
                    return self._handle_json_response(response)
                    
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Erro de conexão: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Erro inesperado: {e}")
            raise

    def _handle_stream_response(self, response) -> str:
        """Processa resposta em streaming"""
        result = ""
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))
                    result += data.get("response", "")
                    
                    if data.get("done", False):
                        break
                        
                except json.JSONDecodeError:
                    self.logger.warning("Linha JSON inválida: %s", line)
        return result.strip()

    def _handle_json_response(self, response) -> str:
        """Processa resposta JSON normal"""
        try:
            data = response.json()
        except json.JSONDecodeError:
            raise ValueError("Resposta não é JSON válido")
            
        if "response" not in data:
            raise ValueError("Resposta do modelo sem campo 'response'")
            
        return data["response"].strip()

    def list_models(self):
        """Lista modelos disponíveis"""
        url = f"{self.base_url}/api/tags"
        try:
            response = self.session.get(
                url, 
                timeout=5,
                headers=self.headers
            )
            response.raise_for_status()
            
            data = response.json()
            if not isinstance(data, dict) or 'models' not in data:
                raise ValueError("Resposta de modelos inesperada")
                
            return [m['name'] for m in data.get('models', [])]
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Erro ao listar modelos: {e}")
            return []
        except (ValueError, KeyError) as e:
            self.logger.error(f"Erro ao processar modelos: {e}")
            return []