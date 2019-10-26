program for arc(graphics)
#include<stdio.h>
#include<graphics.h>
#include<math.h>
#include<conio.h>
void main()
{int gd=DETECT,gm;
initgraph(&gd,&gm,"C:TURBOC3\\BGI");
clrscr();
arc(300,300,0,180,20);
getch();
closegraph();
}
