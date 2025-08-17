#include<stdio.h>
#define M 10
int main(){
    int a[M]={12,11,10,9,8,6,7,6,5,5},i,j;
    for(i=M-1;i>=0;i--){
        int flag=0;
        for(j=0;j<=i;j++)
            if(a[j]>a[j+1]){
                flag=1;
                int temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        if(flag==0)break;
    }
    for(i=0;i< M;i++)printf("%d ",a[i]);
    return 0;
    
}