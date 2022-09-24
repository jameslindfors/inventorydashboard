<script lang="ts">
	import RowForm from './RowForm.svelte';
	export let products;
</script>

<table class="table my-1 is-fullwidth">
	<thead>
		<tr>
			<th>Name</th>
			<th>Price</th>
			<th>Units</th>
			<th>Total Units</th>
			<th>Shipping Rate</th>
			<th>Tax Rate</th>
			<th>Currency</th>
			<th>Sale</th>
			<th>Sale Price</th>
			<th />
			<th />
		</tr>
	</thead>
	<tbody>
		{#each products as product}
			<RowForm {product} />
		{/each}
	</tbody>
</table>
