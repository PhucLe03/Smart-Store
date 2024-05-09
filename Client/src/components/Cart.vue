<template>
    <div>
        <h1 class="text-center p-[50] m-5">Your Cart</h1>
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
    }
}
};
</script>
  
  <style>
  </style>