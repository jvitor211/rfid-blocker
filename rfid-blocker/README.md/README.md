# RFID Blocker Project

Este projeto implementa um sistema de bloqueio RFID com integração entre backend, frontend e hardware. Ele permite bloquear tags RFID, consultar o status de bloqueio e gerenciar dispositivos RFID de forma centralizada.

---

## 🧐 Sobre o Projeto

O **RFID Blocker Project** é um sistema completo para gerenciamento e bloqueio de dispositivos RFID. Ele combina:
- Um **backend** robusto, utilizando **FastAPI**, para gerenciar solicitações.
- Um **frontend** intuitivo, criado com **React**, para facilitar a interação.
- Um **firmware Arduino**, que conecta o sistema ao hardware RFID.

---

## 🚀 Funcionalidades

- **Backend**:
  - API para bloquear e consultar o status de tags RFID.
  - Documentação automática via Swagger.

- **Frontend**:
  - Interface gráfica para interação com o sistema RFID.
  - Formulários e feedback em tempo real.

- **Hardware**:
  - Integração com placas Arduino para leitura e bloqueio de tags RFID.

---

## ✅ Requisitos

### Ferramentas Necessárias

- **Python**: 3.9 ou superior.
- **Node.js**: 16 ou superior.
- **Placa Arduino** (ou compatível com o módulo RFID).
- **Biblioteca MFRC522**: Disponível na IDE Arduino.

### Dependências do Projeto

#### Backend
- Arquivo de dependências: `backend/requirements.txt`.

Instale as dependências:
```bash
pip install -r backend/requirements.txt
