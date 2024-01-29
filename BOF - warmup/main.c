// gcc main.c -o main -no-pie --no-stack-protector

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void setup()
{
  setvbuf(stderr, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
}

void deprecated()
{
  system("/bin/sh");
}

void checkin()
{
  char name[256];
  printf("Name: ");

  scanf("%s", name);
  printf("Welcome, %s\n", name);
}

void main()
{
  setup();

  puts("Welcome, warm your fingers up & go through the checkin");
  checkin();
}