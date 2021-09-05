pizza = int(input('how many pizzas?'))

print("you order" , pizza , "slices")

kids = int(input("how many kids?"))

full_slice_each_kid = pizza // kids

left_over = pizza % kids

print("each kid got " , full_slice_each_kid , "slices" )

print("lesftovers = " , left_over)
