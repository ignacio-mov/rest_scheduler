from scheduler import scheduler, app, commands

scheduler.start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

