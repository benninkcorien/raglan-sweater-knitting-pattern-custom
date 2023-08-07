import math

# Uncomment this if you want it to ask for your measurements each time.

# stitch_gauge = float(input("Enter stitch gauge (stitches for 10 cm): "))
# row_gauge = float(input("Enter row gauge (rows for 10 cm): "))
# how much yarn in cm did you use for 1 row of 10cm wide (unravel and measure)?
# 10cmknitishowmuchyarn = float(input("Enter row gauge (rows for 10 cm): "))
# chestcircumf = float(input("Enter chest circumference in cm: "))
# sleevelength = float(input("Enter sleeve length in cm: "))
# cuff = float(input("Enter cuff circumference in cm: "))
# upperarm = float(input("Enter upper arm circumference in cm: "))
# crewneck = float(input("Enter neck circumference in cm, and then add extra because it's a crewneck (suggestion: 47) : "))
# bodylength = float(input("Enter armpit to hem length in cm: "))
# raglanlength = float(input("Enter armpit to hem length in cm: "))
# waist = float(input("Enter armpit to waist in cm: "))
# chesttowaist = float(input("Enter chest to waist in cm: "))
# hip = float(input("Enter hip circumference in cm: "))

# Or fill out your own measurements here
measurements = {
    "stitch_gauge": 12.5,
    "row_gauge": 16.0,
    "10cmknitishowmuchyarn": 42.0,
    "metersperballofyarn": 70,
    "chestcircumf": 95.0,
    "sleevelength": 52.0,
    "cuff": 21.0,
    "upperarm": 32.0,
    "crewneck": 47.0,
    "bodylength": 52.0,
    "raglanlength": 16.5,
    "waist": 82.0,
    "chesttowaist": 24.0,
    "hip": 96.0,
}

# How many stitches is 10 cm
stitch_gauge = measurements["stitch_gauge"] / 10
# How many rows is 10 cm
row_gauge = measurements["row_gauge"] / 10
# How much yarn do you need to knit 10cm wide (knit, unravel, measure)
howmuchyarnfortencm = measurements["10cmknitishowmuchyarn"]
chestcircumf = measurements["chestcircumf"]
# sleeve length from armpit
sleevelength = measurements["sleevelength"]
cuff = measurements["cuff"]
upperarm = measurements["upperarm"]
# crewneck circ - leave this a bit wide since you knit upwards at the end
crewneck = measurements["crewneck"]
bodylength = measurements["bodylength"]
# raglan length determines how many rows to make from neck to chest
raglanlength = measurements["raglanlength"]
waist = measurements["waist"]
chesttowaist = measurements["chesttowaist"]
hip = measurements["hip"]
metersperballofyarn = measurements["metersperballofyarn"]

# Calculate number of stitches/rows needed based on gauges
chest_stitches = round(stitch_gauge * chestcircumf)
body_length_rows = round(row_gauge * bodylength)
sleeve_length_rows = round(row_gauge * sleevelength)
upper_arm_stitches = round(stitch_gauge * upperarm)
cuff_stitches = round(stitch_gauge * cuff)
neck_stitches = round(stitch_gauge * (crewneck / 1.35))
waist_stitches = round(stitch_gauge * waist)
hip_stitches = round(stitch_gauge * hip)

neckd = round(neck_stitches / 4)
neckc = round(neck_stitches / 2)
necka = round(neckd * 0.22)
neckb = round(neckd * 0.78)
neck_stitches = (necka * 2) + (neckb * 2) + neckc

howmanyneckrows = round(row_gauge * raglanlength)

onecm = measurements["stitch_gauge"] / 10
onestitch = 10 / measurements["stitch_gauge"]

onecminrow = measurements["row_gauge"] / 10
onerowincm = 10 / measurements["row_gauge"]

print(f"One cm is {onecm} stitches")
print(f"One stitch is {onestitch} cm")

print(f"One row is {onerowincm} cm")
print(f"One cm is {onecminrow} row")

# Calculate decreases needed for sleeves from upper arm to cuff
sleeve_decreases = upper_arm_stitches - cuff_stitches

part1 = f"""
## NECK LINE ## 

Cast on {neck_stitches} neck stitches, place markers so it is divided as {necka}, m, {neckb}, m, {neckc}, m, {neckb}, m, {necka}  
KNIT THIS BACK AND FORTH on a straight needle    
{neckb} is the sleeve part, so add rib there if you want it
Raglan Increases:  increases before and after each  marker  
a+2  b+2  c+2 b+2 a+2
R1 (RS): k1, M1, [ k to stitch before marker, kfb, sm, kfb ] 4 times, k to final 2 stitches, M1, k1
R2 (WS): purl all stitches
_ _ _ _ _ _ _ _

Work rows 1 and 2, 3 times (6 rows total) until you have {(necka*2 + 12) + (neckb *2 +12) + neckc + 6 } stitches
({necka + 6} front, {neckc + 6} back, and {neckb + 6}, for each sleeve) ({necka + 6}, {neckb + 6}, {neckc + 6}, {neckb + 6}, {necka + 6})
_ _ _ _ _ _

R7: k{necka + 5}, kfb, sm, kfb, k{neckb + 4}, kfb, sm, kfb, k{neckc + 4}, kfb, sm, kfb, k{neckb + 4}, kfb, sm, kfb, k{necka + 5}, 
This is 8 extra.

Turn your work, cast on 8, place a  marker - this is the center of the front -  cast on 8.
JOIN for knitting in the round. 
The center front marker is now the start of your rounds.
You now have {(necka*2 + 12) + (neckb *2 +12) + neckc + 6 + 24} stitches in total ({necka + 15},  {neckb + 8}, {neckc + 8}, {neckb + 8} {necka + 15}) 
"""

joinedback = neckc + 8
joinedfront = 2 * (necka + 15)
joinedarm = neckb + 8
chestandarmsgoal = chest_stitches + upper_arm_stitches + upper_arm_stitches

startupperbodycount = (joinedfront + joinedback) + (joinedarm * 2)

part2 = f"""
## UPPER  BODY ## 
Work down to the armpits, raglan increases on every second round:
You start with {startupperbodycount} 
arm back arm front ({joinedarm}, {joinedback}, {joinedarm}, {joinedfront}) 
And you need to get to chest and arms combined {chestandarmsgoal}
So you need to add {chestandarmsgoal - startupperbodycount} stitches

You increase 8 stitches every other row, so you need to add {(chestandarmsgoal - startupperbodycount)/8} increases 
this is a total of {(chestandarmsgoal - startupperbodycount)/4} rows added
and for the calculated raglan length from neck to chest, you need {howmanyneckrows} rows  
(so pick a number, input will ask for an int, if you press enter it uses the first value given here) 

"""

text = f"calculated is {(chestandarmsgoal - startupperbodycount)/4} , and gauge is {howmanyneckrows}"
print(text)
howmanyextrarowsfromnecktochest = input("How many rows do you want? > ")
if howmanyextrarowsfromnecktochest is not int:
    howmanyextrarowsfromnecktochest = (chestandarmsgoal - startupperbodycount) / 4

timesa = int(round(howmanyextrarowsfromnecktochest / 2))

roundcounter = round(howmanyextrarowsfromnecktochest) * "_ "
stitchesadded = int(timesa * 8)
fronttotal = int(joinedfront + (timesa * 2))
backtotal = int(joinedback + (timesa * 2))
larmtotal = int(joinedarm + (timesa * 2))
rarmtotal = int(joinedarm + (timesa * 2))
armstotal = larmtotal + rarmtotal

part3 = f"""

## UPPER BODY CONTINUED to ARMPITS
You start with {startupperbodycount} 
arm back arm front
({joinedarm}, {joinedback}, {joinedarm}, {joinedfront}) 

R8(RS): k all stitches 
R9(RS): [ k to 1 st before marker, kfb, sm, kfb ] 4 times, k to center marker, sm 

{roundcounter}

Work rounds 8 and 9, {timesa} times ( {howmanyextrarowsfromnecktochest} rounds total). 
Work round 8 one more time (= knit all). 

# every other row you add 8 stitches
stitches added = {stitchesadded}
front total = {fronttotal}
backtotal = {backtotal}
arm left plus right total = {armstotal} -- arm total goal = {int(upper_arm_stitches)}
You now have  { fronttotal + backtotal + armstotal} stitches in total  -- {chest_stitches + upper_arm_stitches + upper_arm_stitches} (this should match)

Try on your sweater, leave a 8 cm gap under each arm (you'll add {int(onecm * 8) } stitches there). 
"""


part4 = f"""
FINISH THE BODY and separate the sleeves
Knit a round and put the sleeves on a holder.
Add {int(onecm * 8) } stitches under each arm and connect in the round to finish the body.

You start with : {chest_stitches}
You need to get to waist at {waist_stitches} over {chesttowaist} cm. 
Add {chest_stitches - waist_stitches} over  {round(onecminrow * chesttowaist, 2)} rows.
Then add {hip_stitches- waist_stitches} over {round(onecminrow * chesttowaist,2
)} rows.

{body_length_rows } total rows (or until the thing is long enough)
Then add ribbing WITH A SMALLER GAUGE NEEDLE.
"""

startofsleeve = armstotal / 2
decreasetimes = int(math.floor(sleeve_length_rows / ((startofsleeve - upperarm - cuff_stitches) / 2)))
sleeverows = sleeve_length_rows
sleevedecreases = math.floor((startofsleeve + 13 - cuff_stitches) / 2)


part5 = f"""
SLEEVES - knit two at a time.
{startofsleeve} on each sleeve 
Pick up arm stitches, start halfway the underarm stitches you added. 
 
you now have {startofsleeve + int(onecm * 8)} stitches which is {math.floor((startofsleeve + int(onecm * 8)) * onestitch)} cm
Place a marker, join and begin working in the round.
You will knit at total of {sleeve_length_rows} rows

You want to go from {startofsleeve + int(onecm * 8) } to {int(cuff_stitches)} over {sleeve_length_rows} rows with hopefully the uppearm at {int(upperarm)}  stitches (this is NOT written into the pattern since it's usually kinda right if you decrease at even intervals)
You need to decrease {startofsleeve + int(onecm * 8) - cuff_stitches  } stitches over {sleeve_length_rows} rows
and you decrease 2 per decrease row (on each side of the marker)
so there are {sleevedecreases} decrease rows
(really {((startofsleeve + int(onecm * 8) - cuff_stitches ) / 2)} ) so fix the missing stitches somewhere if this is not a nice whole number
"""

decrease_rows = [round((i + 1) * sleeverows / (sleevedecreases + 1)) for i in range(sleevedecreases)]
decrease_text = ", ".join(str(row) for row in decrease_rows)


part6 = f"""
on row {decrease_text} decrease"
{int(sleeve_length_rows) * " _ "}

Decrease once stitch somehwere in the middle if you have an odd number..
Try the sweater on to test your sleeve length, then finish the cuff
SMALLER GAUGE 
Work k1p1 rib for 2.8cm. Bind off.

NECK
Pick up all stitches WITH THE SMALLER GAUGE NEEDLE, 
knit 2x2 rib for 6 rows
"""

# CALCULATE HOW MANY METERS/YARDS of yarn you need, and how many balls that is.
chest_circumference_cm = measurements["chestcircumf"]
body_length_cm = measurements["bodylength"]
onecminrow = onecminrow
howmuchyarnforonecmofknitting = howmuchyarnfortencm / 10

bodypartwidthyarn = chest_circumference_cm * howmuchyarnforonecmofknitting
bodypartrows = bodylength * onecminrow
bodytotalcm = bodypartwidthyarn * bodypartrows

sleeveyarn = ((upperarm + cuff) * 2) * howmuchyarnforonecmofknitting
sleevelenthrows = sleevelength * onecminrow
sleevetotalyarn = sleeveyarn * sleevelenthrows

totalmneeded = ((bodytotalcm + sleevetotalyarn) / 100) * 1.4
# meters = yardage / 91.44
totalyardsneeded = totalmneeded * 1.09361

# totalballs needed
totalballs = totalmneeded / metersperballofyarn

print(
    f"Total meters of yarn needed: {totalmneeded:.2f} meters, this is {totalyardsneeded:.2f} yards, this is {totalballs} balls"
)

 
print(f"Total meters of yarn needed: {yarn_meters_needed:.2f} meters")

pattern_content = f"One cm is {onecm} stitches\nOne sticth is {onestitch} cm\nOne row is {onerowincm} cm\nOne cm is {onecminrow} row\nTotal meters of yarn needed: {totalmneeded:.2f} meters, this is {totalyardsneeded:.2f} yards, this is {totalballs} balls\n\n{part1}\n{part2}\n{part3}\n{part4}\n{part5}\n{part6}"
with open("raglanpattern.txt", "w", encoding="utf-8") as f:
    f.write(pattern_content)
