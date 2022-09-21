function newFunction(n){     
    
    let file_name = ['movie1.jpg','movie2.jpg', 'movie3.jpg', 'movie4.jpg','movie5.jpg','movie6.jpg'];
    
    let i = 0;

    let cnt = 0;
    let output = "";

    let a1 = '<div class="carousel-item active ">';
    let a2 = '<div class="d-flex">';
    let a3 = '<img src="./images/'+file_name[0]+'" style = "padding:10px" alt="">';
    let a4 = '<img src="./images/'+file_name[1]+'" style = "padding:10px" alt="">';
    let a5 = '</div>'+'</div>';

    while(true){
        let tmp = "";
        for(i=cnt;i<cnt+n;i++)
        {
            try{
                tmp+='<img src="./images/'+file_name[i]+'" style = "padding:10px" alt="">';
            }
            catch(e){
                continue
            }
            
        }   

        output+=(a1+a2+tmp+a5);
        cnt+=n;
        

        if(cnt >= 6)
        {            
            break;
        }
            

    } 
    
    document.write(output);
}





// function newFunction_3(){     
    
//     var file_name = ['movie1.jpg','movie2.jpg', 'movie3.jpg', 'movie4.jpg','movie5.jpg','movie6.jpg'];
    
//     var i = 0;

//     var tmp1 = "";

    
    
//     for(i=0;i<3;i++)
//     {
//         tmp1+='<img src="./images/'+file_name[i]+'" style = "padding:10px" alt="">';
//     }   

//     let a1 = '<div class="carousel-item active ">';
//     let a2 = '<div class="d-flex">';
//     let a3 = '<img src="./images/'+file_name[0]+'" style = "padding:10px" alt="">';
//     let a4 = '<img src="./images/'+file_name[1]+'" style = "padding:10px" alt="">';
//     let a5 = '</div>'+'</div>';

    

//     var tmp2 = "";

//     for(i=3;i<6;i++)
//     {
//         tmp2+='<img src="./images/'+file_name[i]+'" style = "padding:10px" alt="">';
//     } 
//     document.write(a1+a2+tmp1+a5+a1+a2+tmp2+a5);
    
// }

function newFunction_2(){     
    
    var file_name = ['movie1.jpg','movie2.jpg', 'movie3.jpg', 'movie4.jpg','movie5.jpg','movie6.jpg'];
    
    var i = 0;


    let a1 = '<div class="carousel-item active ">';
    let a2 = '<div class="d-flex">';
    let a3 = '<img src="./images/'+file_name[0]+'" style = "padding:10px" alt="">';
    let a4 = '<img src="./images/'+file_name[1]+'" style = "padding:10px" alt="">';
    let a5 = '</div>'+'</div>';


    var tmp1 = "";

    for(i=0;i<2;i++)
    {
        tmp1+='<img src="./images/'+file_name[i]+'" style = "padding:10px" alt="">';
    }   

  
    
    document.write(a1+a2+tmp1+a5+a1+a2+tmp2+a5);




    var tmp2 = "";

    for(i=2;i<4;i++)
    {
        tmp2+='<img src="./images/'+file_name[i]+'" style = "padding:10px" alt="">';
    } 
    document.write(a1+a2+tmp1+a5+a1+a2+tmp2+a5);


    var tmp3= "";

    for(i=4;i<6;i++)
    {
        tmp2+='<img src="./images/'+file_name[i]+'" style = "padding:10px" alt="">';
    } 
    document.write(a1+a2+tmp3+a5+a1+a2+tmp2+a5);
    
}

function newFunction_1(){     
    
    var file_name = ['movie1.jpg','movie2.jpg', 'movie3.jpg', 'movie4.jpg','movie5.jpg','movie6.jpg'];
    
    var i = 0;

    let a1 = '<div class="carousel-item active ">';
    let a2 = '<div class="d-flex">';
    let a3 = '<img src="./images/'+file_name[0]+'" style = "padding:10px" alt="">';
    let a4 = '<img src="./images/'+file_name[1]+'" style = "padding:10px" alt="">';
    let a5 = '</div>'+'</div>';



    var output = "";

    for(i=0;i<6;i++)
    {
        output+=(a1+a2+'<img src="./images/'+file_name[i]+'" style = "padding:10px" alt="">'+a5);
    }   

    document.write(a1+a2+tmp1+a5+a1+a2+tmp2+a5);
    
}
