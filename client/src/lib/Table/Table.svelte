<script lang="ts">
	import type { ProductType } from '../../types/product.type';
	import { enhance } from '$app/forms';

	// @ts-expect-error Import Issue
	import { Snackbar } from 'svelma';

	import TableRow from '$lib/TableRow/TableRow.svelte';

	export let products: ProductType[];
	let editing = false;
</script>

<div class="table is-fullwidth">
	<div class="tr">
		<span class="td">Name</span>
		<span class="td">Price</span>
		<span class="td">Units</span>
		<span class="td">Total Units</span>
		<span class="td">Shipping Rate</span>
		<span class="td">Tax Rate</span>
		<span class="td">Currency</span>
		<span class="td">Sale</span>
		<span class="td">Sale Percent</span>
		<span class="td">Edit</span>
		<span class="td">Delete</span>
	</div>

	{#each products as product}
		<form
			class="tr"
			method="POST"
			action="?/update"
			use:enhance={({ form, data, cancel }) => {
				return ({ result }) => {
					if (result.type === 'success') {
						editing = false;

						Snackbar.create({
							message: 'Product updated successfully',
							type: 'is-info',
							position: 'is-bottom-right',
							queue: false,
							duration: 3000
						});
					} else {
						editing = false;
						
						Snackbar.create({
							message: 'Product update failed',
							type: 'is-danger',
							position: 'is-bottom-right',
							queue: false,
							duration: 3500
						})
					}
				};
			}}
		>
			<TableRow {product} {editing} />
			<input type="hidden" name="product_id" value={product.id} />
		</form>
	{/each}
</div>

<style>
	DIV.table {
		display: table;
		width: 100%;
	}
	FORM.tr,
	DIV.tr {
		display: table-row;
	}
	SPAN.td {
		display: table-cell;
		padding: 0.5em;
	}
</style>
