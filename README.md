# 🚑 Self-Healing Infrastructure using Prometheus, Alertmanager & Ansible

This project demonstrates a **self-healing infrastructure** that automatically detects service failures (like a downed NGINX server) using Prometheus alerts and triggers an **Ansible playbook** via a Flask-based webhook to restart the failed service.

---

## 📦 Tech Stack

- **Docker + Docker Compose**
- **NGINX** – Simulated web service
- **Prometheus** – Monitoring and alerting
- **Alertmanager** – Sends alerts to webhook
- **Flask Webhook Server** – Receives alert and triggers Ansible
- **Ansible** – Restarts failed container

---

## 📁 Project Structure

![image](https://github.com/user-attachments/assets/dae5327a-e7b4-4f61-929d-f0cb40b3914b)


---

## 🚀 How It Works

1. **Prometheus** scrapes metrics from NGINX exporter.
2. If NGINX goes down or exporter becomes unreachable, an **alert** is fired.
3. **Alertmanager** forwards the alert to a **Flask webhook**.
4. The **webhook** triggers an **Ansible playbook** that restarts the `nginx` Docker container.

---

## ⚙️ Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/Raj9536/self-healing-infrastructure-with-prometheus.git
cd self-healing-infra
```
### 2. Build & Start Containers
```
docker-compose up --build
```
### 3. Stop NGINX container to simulate failure
```
docker stop self-healing-infra-nginx-1
```
Within ~30s:

- Prometheus detects the failure.
- Alertmanager sends alert to Flask.
- Flask triggers Ansible.
- Ansible restarts NGINX automatically 🚑

### 🔍 Monitoring Interfaces
Tool	URL
Prometheus	http://localhost:9090

Alertmanager	http://localhost:9093

NGINX App	http://localhost:8080

Webhook (Flask)	http://localhost:5001

### 📸 Screenshots
You can take screenshots of:

Prometheus Alerts tab

![Screenshot 2025-04-28 213236](https://github.com/user-attachments/assets/8e7c0a2d-2b02-4fa2-bf0a-6245a8a67539)

Nginx gets Down

![Screenshot (12)](https://github.com/user-attachments/assets/7bbbfc1e-f1d3-46d0-96f4-b6cc57785ca1)

Prometeus Showing the firing state

![Screenshot 2025-04-28 213325](https://github.com/user-attachments/assets/2639e1bb-90ae-4452-a17d-a842897e2627)


Restarting the Nginx (Up)

![Screenshot 2025-04-27 084833](https://github.com/user-attachments/assets/b76c3b24-9d22-4263-adc1-4107d6d46e79)

Browser image

![Screenshot 2025-04-28 212759](https://github.com/user-attachments/assets/3a031fe0-23fd-49dd-88f7-2037f7eee8ef)

Docker showing container restarted

![Screenshot 2025-04-28 213014](https://github.com/user-attachments/assets/0e08c3d1-4e53-4e93-b7fc-7fe479bd26d9)

Alertmanager

![Screenshot 2025-04-28 212932](https://github.com/user-attachments/assets/ee918050-3e83-4541-977e-baf569d4664b)

### ✅ Testing Webhook Manually
```
curl -X POST http://localhost:5001/alert -H "Content-Type: application/json" -d '{"test":"ok"}'
```
You should see:
```
Received Alert: {'test': 'ok'}
```

### 🧠 Concepts I had learned
1. Infrastructure Monitoring

2. Alert Rules in Prometheus

3. Alert Routing in Alertmanager

4. Triggering Automation from Alert

5. Docker + Ansible integration


### 🙌 Acknowledgements
Prometheus & Alertmanager docs

Flask for simplicity

Ansible for infrastructure automation
