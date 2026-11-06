module.exports = {
  apps: [{
    name: "flask-backend",
    script: "venv/bin/gunicorn",
    args: "-w 2 -b 0.0.0.0:5000 app:app",
    interpreter: "none",
    cwd: __dirname
  }]
};
