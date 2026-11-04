# Devops Project 3

## Используемый стек

- **Ansible 2.9.6** — управление конфигурацией
- **Docker**, **Docker Compose** — контейнеризация
- **Prometheus 2.51.0** — сбор и хранение метрик
- **Grafana 10.4.0** — визуализация
- **Node Exporter 1.7.0** — системные метрики
- **cAdvisor 0.47.2** — метрики контейнеров

## О проекте

Проект демонстрирует **инфраструктуру как код (IaC)** и **управление конфигурацией** с помощью Ansible. Разворачивает полный стек:

- **Приложение** (Flask + PostgreSQL + Nginx) — из [Проекта 2](https://github.com/LLoylento4bIx4ervei/devops-project2).
- **Мониторинг** (Prometheus + Grafana + Node Exporter + cAdvisor).

Всё разворачивается **одной командой** `ansible-playbook playbooks/site.yml`.
