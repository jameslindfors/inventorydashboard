<script lang="ts">
	import type { ProductType } from 'src/types/product.type';
	import RowForm from '../RowForm/RowForm.svelte';
	export let products: ProductType[];
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
			<th>Sale Percent</th>
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
