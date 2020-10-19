## longest increasing subsequence
l=list(map(int,input().split()))
## using dp

dp=[1 for i in range(len(l))]

for i in range(1,len(l)):

    j=0

    for j in range(i):

        if(l[i]>l[j]):

            
            
            dp[i]=max(dp[j]+1,dp[i])


n=max(dp)
print(n)

len1=dp.index(max(dp))


num=l[dp.index(max(dp))]


st=[]

st.append(l[dp.index(max(dp))])
while(len1>=0):
    

    if(dp[len1]+1==n and l[len1]<num):

        st.append(l[len1])

        n=dp[len1]

        num=l[len1]
    len1-=1

st.reverse()

print(*st)








    


    
