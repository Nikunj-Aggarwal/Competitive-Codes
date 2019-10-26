//program for circle(graphics)
#include<stdio.h>
#include<graphics.h>
#include<math.h>
#include<conio.h>
void main()
{int gd=DETECT,gm;
initgraph(&gd,&gm,"C:TURBOC3\\BGI");
clrscr();
circle(100,100,10);
getch();
closegraph();
}
