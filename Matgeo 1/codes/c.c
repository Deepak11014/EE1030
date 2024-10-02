#include <stdio.h>
#include <math.h>

int main() {
    // Speed of rain (downward) and woman (southward)
    float v_rain = -30.0;  // Vertical speed of rain in m/s
    float v_woman = 10.0; // Woman's speed (north to south) in m/s

    // Calculate the angle using the arctangent function
    float angle_radians = atan(v_woman / v_rain);
    
    // Convert the angle from radians to degrees
    float angle_degrees = angle_radians * (180.0 / M_PI);
    
    // Open a text file to save only the angle
    FILE *file = fopen("angle.txt", "w");

    // Check if the file was opened successfully
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    // Write only the angle to the file
    fprintf(file, "%.2f\n", angle_degrees);  // Write just the angle in degrees

    // Close the file
    fclose(file);
    
    printf("The angle has been written to angle.txt\n");

    return 0;
}

