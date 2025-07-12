# Main.py
'''
The chat bot feature was developed and adapted from an online YouTube tutorial [1]. The base functionality the gets the response and
checks the messages was from the tutorial. I extended it to produce a formatted string response, that is subsequently parsed to 
allow for specific information to be displayed.
[1] Indently (2021) "How to create an accurate Chat Bot Response System in Python Tutorial (2021)". https://www.youtube.com/watch?v=Ea9jgBjQxEs. Accessed on: 02/07/2025
'''
import sys
import scripts.app as app

if __name__ == "__main__":
    # Ensure the app is initialized and run
    try:
        application = app.app()
    except Exception as e:
        print(f"An error occurred while starting the application: {e}", file=sys.stderr)
        sys.exit(1)