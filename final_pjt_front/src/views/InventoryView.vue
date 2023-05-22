<template>
  <div class="InventoryView">
    <div class="username">
      <h1 id="username">알렉스킴</h1>
      <h2>의 인벤토리</h2>
    </div>
    <FirstChingho />
    <LastChingho />
    <MixChingho />
  </div>
</template>

<script>
import FirstChingho from "@/components/Inventory/FirstChingho";
import LastChingho from "@/components/Inventory/LastChingho";
import MixChingho from "@/components/Inventory/MixChingho";
export default {
  name: "InventoryView",
  components: {
    FirstChingho,
    LastChingho,
    MixChingho,
  },
};
</script>
<style scoped>
.InventoryView {
  margin-top: 70px;
  margin-left: 200px;
  background-color: black;
  padding: 50px;
}
.username {
  display: flex;
  align-items: baseline;
}
#username {
  font-size: 60px;
}
</style>
