using System;
using static System.Console;

public class Room
{
	const int x = 2;
	const int y = 3;
	static void Main(string[] args)
	{
		chartedRoom();
	}
	//Shows the room on screen
	public static void chartedRoom()
	{
		WriteLine("(1,1)|(1,2)|(1,3)|(1,4)");
		WriteLine("(2,1)|(2,2)|(2,3)|(2,4)");
		WriteLine("(3,1)|(3,2)|(3,3)|(3,4)");
		WriteLine("(4,1)|(4,2)|(4,3)|(4,4)");
	}
	
	//Sets bounderies around the square
	public static int Bounderies()
	{
		if (x > 4 | x < 0)
		{
			WriteLine("You've hit a wall");
			if(x = 5)
			{
				x -= 1;
			}
			else if(x = -1)
			{
				x += 1;
			}
		}
		if (y > 4 | y < 0)
		{
			WriteLine("You've hit a wall");
			if(y = 5)
			{
				y -= 1;
			}
			else if(y = -1)
			{
				y += 1;
			}
		}
		
	}
}