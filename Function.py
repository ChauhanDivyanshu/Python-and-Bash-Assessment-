# Create or open a file in write mode
file = open("myfile.txt", "w")

# Write content to the file
file.write("Hello, this is a sample text written to the file.\n")
file.write("This is the second line of the file.\n")
file.write("This is Divyanshu Chauhan and I am a new learner of DevOps")

# Close the file
file.close()

print("Content written successfully to 'myfile.txt'.")
