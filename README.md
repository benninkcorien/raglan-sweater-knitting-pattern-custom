#  Customizable Knitting Pattern Generator for a Raglan Sweater
A python script that generates a raglan sweater based on your measurements and gauge
(this script is intentionally a bit of a mess, so it's easy to change things.)

## Enter measurements

- stitch_gauge =  stitches for 10 cm 
- row_gauge = rows for 10 cm 
- 10cmknitishowmuchyarn how much yarn in cm did you use for 1 row of 10cm wide (unravel and measure) 
- chestcircumf =  chest circumference in cm 
- sleevelength = sleeve length in cm
- cuff = cuff circumference in cm
- upperarm = upper arm circumference in cm
- crewneck = neck circumference in cm plus extra (you make it narrower at the end.. 47 default seems to work)
- bodylength = armpit to hem length in cm
- raglanlength = neck to armpit length in cm
- metersperballofyarn = How many meters of yarn in 1 ball



Enter your measurements in cm here:

        measurements = {
            "stitch_gauge": 12.5,
            "row_gauge": 16.0,
            "10cmknitishowmuchyarn": 42.0,
            "metersperballofyarn": 70.0,
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
Or comment that out and use the inputs

## How much yarn is needed

Knit 10 cm, unravel and measure in cm how much yarn you used to do that. This is used to calculate the total needed.
(Tested for accuracy with 1 sweater. This script returns slightly more than used.)

## Keep track of rows
The pattern also contains _ _ _ placeholders so you can keep track of how many rows you've knit.
