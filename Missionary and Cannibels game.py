from IPython.display import clear_output
boat_side='right'
missionaries_on_right= 3
cannibals_on_right= 3
missionaries_on_left=0
cannibals_on_left=0

print('\U0001f482'*missionaries_on_left,'\U0001f479'*cannibals_on_left,'|','\U0001f30a'*4,'\U0001f6A2',' |','\U0001f482'*missionaries_on_right,'\U0001f479'*cannibals_on_right)



while True:
  print('enter no of m & c on the boat ')
  print('enter the no missionaries')
  missionaries=int(input())
  print('enter the no canibals')
  cannibals=int(input())
  if missionaries + cannibals !=1 and missionaries + cannibals !=2 :
     print('invalid move ')

     continue
  if boat_side == 'right':
      print('|','\U0001f30a'*4,'\U0001f6A2','|')

      if (missionaries > missionaries_on_right) or (cannibals > cannibals_on_right) :
        print('invalid move')
        continue
      missionaries_on_right-=missionaries
      missionaries_on_left+=missionaries
      cannibals_on_right-=cannibals
      cannibals_on_left+=cannibals
      boat_side='left'
      print(1)
      print('\U0001f482'*missionaries_on_left,'\U0001f479'*cannibals_on_left,'|','\U0001f6A2','\U0001f30a'*4,' |','\U0001f482'*missionaries_on_right,'\U0001f479'*cannibals_on_right)

  elif boat_side=='left':
      print('|','\U0001f6A2','\U0001f30a'*4,'|')
 
      if missionaries>missionaries_on_left or cannibals>cannibals_on_left:
        print('invalid move 2')
        continue
      missionaries_on_left=missionaries_on_left-missionaries
      cannibals_on_left=cannibals_on_left-cannibals
      missionaries_on_right=missionaries_on_right+missionaries
      cannibals_on_right=cannibals_on_right+cannibals
      boat_side='right'
      print('\U0001f482'* missionaries_on_left , '\U0001f479'*cannibals_on_left,'|','\U0001f30a'*4,'\U0001f6A2','|','\U0001f482'*missionaries_on_right,'\U0001f479'*cannibals_on_right)
      print(2)
  if missionaries_on_left==3 and cannibals_on_left==3:
    print('YOU WIN !!!!!')
    break
  if missionaries_on_right<cannibals_on_right and missionaries_on_right>0 or missionaries_on_left<cannibals_on_left and missionaries_on_left>0:
    print('YOU LOSE ')
    break