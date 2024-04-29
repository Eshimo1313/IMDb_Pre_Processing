up:
	docker compose up -d --build

start:
	docker compose start

stop:
	docker compose stop

ui:
	streamlit run ./script/UI.py
