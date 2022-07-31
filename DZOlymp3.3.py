k = int(input())
ed = k % 10
dec = k // 10 % 10
if ed == 1 and dec != 1:
    print("Mne", k, "god")
elif (1 < ed < 5) and dec != 1:
    print("Mne", k, "goda")
else:
    print("Mne", k, "let")