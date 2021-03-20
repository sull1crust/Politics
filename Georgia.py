raw = ( """
Raphael Warnock
Democrat
1,616,973	32.9
Kelly Loeffler
Republican
1,273,188	25.9
Doug Collins
Republican
980,457	20.0
Deborah Jackson
Democrat
324,126	6.6
Matt Lieberman
Democrat
136,015	2.8
Tamara Johnson-Shealey
Democrat
106,771	2.2
Jamesia James
Democrat
94,406	1.9
Derrick Grayson
Republican
51,595	1.0
Joy Slade
Democrat
44,946	0.9
Annette Jackson
Republican
44,334	0.9
Kandiss Taylor
Republican
40,349	0.8
Wayne Johnson
Republican
36,173	0.7
Brian Slowinski
Libertarian
35,431	0.7
Richard Winfield
Democrat
28,688	0.6
Ed Tarver
Democrat
26,333	0.5
Allen Buckley
Independent
17,955	0.4
John Fortuin
Green
15,293	0.3
Al Bartell
Independent
14,640	0.3
Valencia Stovall
Independent
13,318	0.3
Michael Greene
Independent
13,292	0.3
""")

raw = raw.split("\n")

del raw[0]
del raw[(int(len(raw)))-1]

print("Here are the candidates, their parties, and how many votes each received in November...")
raw_cleaned = []
for line in raw:
    line = line.split("\t")[0]
    print(line)
    line = line.replace(',', '')
    raw_cleaned.append(line)

Republican_votes = 0
Democrat_votes = 0
Other_votes = 0

for line in raw_cleaned:
    index = raw_cleaned.index(line)
    if line == "Republican":
        Republican_votes += int(raw_cleaned[index + 1])
        raw_cleaned.pop(index)
    elif line == "Democrat":
        Democrat_votes += int(raw_cleaned[index + 1])
        raw_cleaned.pop(index)
    elif line == "Libertarian":
        Other_votes += int(raw_cleaned[index + 1])
        raw_cleaned.pop(index)
    elif line == "Independent":
        Other_votes += int(raw_cleaned[index + 1])
        raw_cleaned.pop(index)

print ("\n" + "Total Republican votes: " + str(Republican_votes))
print ("Total Democrat votes: " + str(Democrat_votes))
print ("Total other votes: " + str(Other_votes))

print("\n")

if Republican_votes > Democrat_votes:
    print ("Republicans will likely win the Georgia primary, if voting behaviour doesn't change much from November.")
    print ("If everyone votes for the candidate of the same party for which they voted before, it'll be a margin of " + str(Republican_votes - Democrat_votes) + " votes.")
else:
    print ("As you can see, if voting behaviour doesn't change, Democrats may well bring about an upset in January's primary.")
    print ("If everyone votes for the candidate of the same party for which they voted before, it'll be a margin of " + str(Democrat_votes - Republican_votes) + " votes.")

print ("But this is discounting the Libertarian and Independent votes...")

print ("\n")

Republican_votes_new = Other_votes*(1/3)+Republican_votes
Democrat_votes_new = Other_votes*(2/3)+Democrat_votes

print ("If Libertarians and Independents break two thirds for Raphael, the final tally will be:" + "\n")

print ("Republican votes: " + str(round(Republican_votes_new)))
print ("Democrat votes: " + str(round(Democrat_votes_new)))

if Republican_votes_new > Democrat_votes_new:
    print("Republicans still win!")
else:
    print("Dems upset!")
