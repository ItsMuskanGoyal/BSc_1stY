window.addEventListener('load', () => {

    const 




    const product = {
        'abc': {
            title: 'pr1',
            desc: "some"
        },
        'arbc': {
            title: 'pr2',
            desc: "some"
        },
        'abcd': {
            title: 'pr12',
            desc: "some"
        },
        'abvc': {
            title: 'pr4',
            desc: "some"
        }
    }


    let productContainer = document.getElementById('products-container');
    let selectedNames = ['abc','abcd', 'abvc', 'arbc']
    createCards(selectedNames, productContainer);

    console.log(productContainer, 'container')

    //search
    let searchElement = document.getElementById('search-box');
    console.log(searchElement, 'search');
    searchElement.addEventListener('search', ()=>{
        console.log(searchElement, 'value');
        for (let index = 0; index<product.length; index++){
            const element = products[index];
            console.assert
            let pname= 
        }
        
        });
    });
    



});

//let is local, var is global, const is constant
//locoend javascript book
//
