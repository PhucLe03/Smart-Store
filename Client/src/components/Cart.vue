<template>
    <div>
        <h1 class="text-center p-[50] m-5">Your Cart</h1>
        <div class="justify-center relative m-5">
            <button v-on:click="clearCart()" class="m-auto block text-center appearance-none bg-transparent box-border text-[#3B3B3B] cursor-pointer text-base font-semibold leading-[normal] min-h-[3.75em] min-w-0 text-center no-underline transition-all duration-300 ease-[cubic-bezier(.23,1,0.32,1)] select-none touch-manipulation will-change-transform px-[2.3em] py-[1em] rounded-[0.9375em] border-[0.125em] border-solid border-[#1A1A1A] disabled:pointer-events-none hover:text-white hover:bg-[#1A1A1A] hover:shadow-[rgba(0,0,0,0.25)_0_8px_15px] hover:-translate-y-0.5 active:shadow-none active:translate-y-0">clearCart</button>
        </div>
        <div class="grid grid-cols-[repeat(4,223px)] gap-[30px] justify-center">
            <div v-for="(product, index) in cart" :key="index" class="rounded border-2 border-solid border-[#212529] flex flex-col justify-between">
                <img class="w-220 h-220" :src="product.image" />
                <div class="flex flex-col gap-2.5 p-2.5 justify-between">
                    <h3><strong>{{product.name}}</strong></h3>
                    <div class="flex flex-row justify-between items-center object-bottom">
                        <h2><strong>{{product.cost}}</strong></h2>
                        <button class="bg-[black] text-[white] cursor-pointer p-2.5 border-[none]" v-on:click="removeItemFromCart(product)">Remove from cart</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
export default {
props: ["cart"],
methods: {
    removeItemFromCart(product) {
        this.$emit("removeItemFromCart", product);
    },
    // checkCart() {
    //     if (this.cart.length > 0) {
    //         return true;
    //     } else {
    //         return false;
    //     }
    // },
    clearCart() {
        this.$emit("clearCart");
    }
}
};
</script>
  
  <style>
  </style>