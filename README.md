# RFID Blocker 🛡️

**RFID Blocker** é uma solução completa para gerenciamento e bloqueio de dispositivos RFID. Este projeto combina um backend robusto, uma interface web intuitiva e integração com hardware para oferecer segurança em aplicações que utilizam tecnologia RFID.

---

## 🔖 Sobre o Projeto

A crescente adoção de dispositivos RFID traz novos desafios relacionados à segurança. O **RFID Blocker** foi desenvolvido para:
- Bloquear tags RFID não autorizadas.
- Monitorar o status das tags em tempo real.
- Oferecer uma interface amigável para controle de dispositivos.
- Conectar-se diretamente a módulos RFID usando Arduino.

---

## 💡 Funcionalidades

- **Bloqueio de Tags RFID**: Impede o uso de tags não autorizadas.
- **Consulta de Status**: Verifica se uma tag está bloqueada ou ativa.
- **Interface Gráfica**: Gerencie dispositivos de maneira visual.
- **Integração com Hardware**: Suporte para módulos RFID e placas Arduino.

---

## 🕰️ Estrutura do Projeto

```plaintext
rfid-blocker/
├── backend/         # Backend com FastAPI
│   ├── app/         # Lógica da API
│   ├── main.py      # Ponto de entrada
│   ├── requirements.txt # Dependências
├── frontend/        # Frontend com React
│   ├── src/         # Código-fonte
│   └── App.jsx      # Componente principal
├── hardware/        # Código do firmware para RFID
│   └── firmware/    # Código Arduino
├── scripts/         # Scripts auxiliares
│   └── setup.sh     # Script de configuração
└── README.md        # Documentação do projeto
```

---

## ✅ Requisitos

### Ferramentas Necessárias

- **Python**: 3.9 ou superior.
- **Node.js**: 16 ou superior.
- **Arduino IDE**: Para carregar o firmware no hardware.
- **Placa Arduino** e **Módulo RFID** compatível.

---

## 🚀 Configuração

### 1. Clone o Repositório

```bash
git clone https://github.com/seuusuario/rfid-blocker.git
cd rfid-blocker
```

---

### 2. Configurar o Backend

1. Navegue para a pasta `backend`:
   ```bash
   cd backend
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Acesse a API no navegador:
   - Documentação Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 3. Configurar o Frontend

1. Navegue para a pasta `frontend`:
   ```bash
   cd frontend
   ```
2. Instale as dependências:
   ```bash
   npm install
   ```
3. Execute o servidor:
   ```bash
   npm start
   ```
4. Acesse a interface gráfica:
   - [http://localhost:3000](http://localhost:3000)

---

### 4. Configurar o Hardware

1. Conecte o módulo RFID à placa Arduino:
   - **SS_PIN**: Pino digital 10.
   - **RST_PIN**: Pino digital 9.
2. Abra a IDE Arduino.
3. Carregue o firmware localizado em `hardware/firmware/rfid_controller.ino`.
4. Use o monitor serial para verificar o funcionamento.

---

## 🎮 Como Usar

1. **Bloquear uma Tag**:
   - Acesse a interface ou envie uma solicitação para o endpoint `/api/rfid/block`.
2. **Consultar o Status**:
   - Use o endpoint `/api/rfid/status/{tag_id}` para verificar o status de uma tag.
3. **Monitorar Dispositivos**:
   - Visualize as leituras diretamente no monitor serial da IDE Arduino.

---

## 🛡️ Segurança

- Todas as requisições API utilizam métodos HTTP seguros.
- Certifique-se de rodar o projeto em um ambiente protegido (por exemplo, com HTTPS configurado).

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga estas etapas para contribuir:

1. Faça um Fork do projeto.
2. Crie uma Branch para sua Feature:
   ```bash
   git checkout -b feature/NovaFeature
   ```
3. Faça Commit de suas alterações:
   ```bash
   git commit -m "Adicionei uma NovaFeature"
   ```
4. Faça Push para a Branch:
   ```bash
   git push origin feature/NovaFeature
   ```
5. Abra um Pull Request.

---

## 🖋️ Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## 📢 Contato

- **Autor**: [John R]
- **Email**: [sinopse0102@gmail.com]

