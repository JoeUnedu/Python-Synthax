def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

     # this line check for the unit in or out  if is a match 
     # perhaps it convert to lower case in case
    if ((unit_in.lower()== "f") or (unit_in.lower()== "c")):   
         if ((unit_out.lower() == "f") or (unit_out.lower()=="c")):
          # if it is not a match we can perform conversion
            if((unit_in.lower() != unit_out.lower())):
              # if unit in is a match for fareinherit let us perfom a conversion now
              if (unit_in.lower() == "f"):
                 #convert from farenheit to celcious
                return round(((temp-32) * 5/9),1)
              else:
                # convert to celcious to farenheit
                 return round(((temp * 9/5) +32),1)
                 # if unit_in = unit_out no need for conversion, return temp
            else:   
                  return temp
         else:

            return f"Invalid unit [UNIT_OUT]{unit_out}"

    else:
      return f"Invalid  unit [UNIT_IN]{unit_in}"




print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

