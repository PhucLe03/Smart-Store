<template>
    <div>
        <header>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
            <div class="flex flex-row justify-between">
                <button class="text-center p-[50] ml-5 mr-5" v-on:click="navigateTo('products')">View products</button>
                <div class="text-center p-[50] ml-5 mr-5">
                    <div class="relative bg-white text-[#212529] text-3xl rounded p-[5px]">
                        <button class="bi bi-cart2 " v-on:click="navigateTo('cart')"></button>
                    </div>
                    <p>{{cart.length}} in cart</p>
                </div>
            </div>
        </header>
    
        <div v-if="page === 'cart'">
            <Cart v-on:removeItemFromCart="removeItemFromCart" :cart="cart" />
        </div>
    
        <div v-if="page === 'products'">
          <Products v-on:addItemToCart="addItemToCart" />
        </div>
    </div>
</template>
  
<script>
import Products from "../components/Products.vue";
import Cart from "../components/Cart.vue";

export default {
    name: "shopping",
    data: () => {
        return {
            page: "products",
            cart: []
        };
    },
    methods: {
        addItemToCart(product) {
            this.cart.push(product);
        },
        removeItemFromCart(product) {
            this.cart.splice(this.cart.indexOf(product), 1);
        },
        navigateTo(page) {
            this.page = page;
        }
    },
    components: { Products, Cart }
};
</script>
  
  <!-- <style>
  body {
    margin: 0;
  }
  
  .products {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
  
  .products button {
    padding: 10px;
    background-color: black;
    color: white;
    outline: none;
    border: none;
    cursor: pointer;
  }
  </style>
  
  <style scoped>
  header {
    height: 60px;
    box-shadow: 2px 2px 5px blue;
    background-color: pink;
    text-align: right;
    font-size: 30px;
    padding-top: 20px;
  }
  
  header button {
    padding: 10px;
    border: none;
    cursor: pointer;
    color: white;
    background-color: green;
  }
  </style> -->

