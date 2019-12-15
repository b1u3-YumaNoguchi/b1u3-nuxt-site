<template>
  <div>
    <h1>
      UPDATED
    </h1>
    <v-simple-table dense fixed-header class="mb-2" style="border: thin solid;">
      <thead>
        <tr>
          <th class="text-left">
            Updated&nbsp;Posts
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(post_name, index) in $store.state.updated_posts" :key="index">
          <td>
            {{ post_name }}
          </td>
        </tr>
        <tr>
          <td>
            Updated&nbsp;post1
          </td>
        </tr>
        <tr>
          <td>
            Updated&nbsp;post2
          </td>
        </tr>
        <tr>
          <td>
            Updated&nbsp;post3
          </td>
        </tr>
      </tbody>
    </v-simple-table>
  </div>
</template>

<script>
export default {
}
</script>
