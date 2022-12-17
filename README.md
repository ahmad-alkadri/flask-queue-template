# Flask-queue Template

A template repo for Flask web REST API with queue system using RQ module.

To load the example application, simply clone this repo by typing the following on your Terminal:

```bash
git clone https://github.com/LekoLabs/flask-queue-template.git flask-queue-template
```

Then, `cd` to the `flask-queue-template` directory and launch the `boot.sh`:

```bash
cd flask-queue-template
./boot.sh
```

Inside the `boot.sh`, there are three parts of important commands. The first one will check if `redis-stack-server` exists and running in
your docker or not. If not, it'll pull it from docker hub and run it:

```bash
if [ $( docker ps -a | grep redis-stack-server | wc -l ) -gt 0 ]; then
  echo "redis-stack-server exists and running"
else
  echo "redis-stack-server does not exist, running it now"
  docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
fi
```

In the second part, it'll check if there's already a local Python environment called `.locenv` or not. If not,
it'll create it using `virtualenv` (it'll install this module if it doesn't exist yet), then create said
virtual environment, and activate it, then install all the necessary requirements. If it found the local environment,
it'll then simply activate it and install the necessary requirements.

```bash
if [ ! -f .locenv/bin/activate ]
then
    echo "Local environment isn't found. Initiating..."
    python3 -m pip install virtualenv
    python3 -m virtualenv .locenv
    source .locenv/bin/activate
    python3 -m pip install -r requirements.txt
else
    echo "Local environment found. Activating it..."
    source .locenv/bin/activate
    python3 -m pip install -r requirements.txt
fi
```

Finally, it'll activate the flask web-app, together with the RQ worker:

```bash
./app.py
```

Which then you can test out. Sample POSTMAN collection calls are available on the `examplecall` directory.

---

Questions? Problems? Feel free to raise them as Issues or contact me directly.

---
