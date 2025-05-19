def log_emotion(emotion, logfile="emotions.log"):
    with open(logfile, "a") as f:
        f.write(f"{emotion}\n")
