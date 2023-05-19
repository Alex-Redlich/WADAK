<template>
  <div class="InventoryView">
    <h1>Inventory Page</h1>
    <FirstChingho />
    <LastChingho />
    <MixChingho />
  </div>
</template>

<script>
import FirstChingho from "@/components/Inventory/FirstChingho"
import LastChingho from "@/components/Inventory/LastChingho"
import MixChingho from "@/components/Inventory/MixChingho"
export default {
  name: "InventoryView",
  components: {
    FirstChingho,
    LastChingho,
    MixChingho,
  },
}
</script>
