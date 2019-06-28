#include<stdio.h>
main()
{
	int first=0,second=1,third,i,n;
	printf("Enter the number of terms :");
	scanf("%d",&n);
	printf("The fibonnacci series is  %d %d ",first,second);
	for(i=0;i<n-2;i++)
	{
		third=first+second;
		first=second;
		second=third;
		printf("%d ",third);
	}
}
