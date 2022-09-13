var added_item_count = 0;
let nomal_price =[0,2000,3000,4000,5000]
let discount_price = [0,1000,3000,3000,5000]


function print_item_count(){

    document.write(added_item_count);

}

function price(item_num){
 
    
    

    if(nomal_price[item_num] == discount_price[item_num])
    {
        alert(nomal_price[item_num]);
    }
    else
    {
        alert("<del>",nomal_price[item_num],"</del>","&nbsp;&nbsp;",discount_price[item_num]);
    }
      
}

