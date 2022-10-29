# %% [markdown]
# Always Remember To Take A Break Dude!

# %%
import time
import webbrowser

breaks = 2
n = int(input("Enter the number of hours in between two successive breaks: "))

for i in range(breaks):
    time.sleep(n*60*60)
    webbrowser.open('https://www.youtube.com/',new=2)