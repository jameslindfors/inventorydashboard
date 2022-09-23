<script lang="ts">
	import { EditIcon, Trash2Icon } from 'feather-icons-svelte-kit';
	export /**
	 * @type {any}
	 */
	let products;
</script>

<table class="table mx-4 my-1 is-fullwidth">
	<thead>
		<tr>
			<th
				>Name
				<span class="icon is-small">
					<a href="/click">
						<EditIcon />
					</a>
				</span>
			</th>
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
			<tr>
				<td>{product.name}</td>
				<td>${product.price}</td>
				<td>{product.current_units}</td>
				<td>{product.total_units}</td>
				<td>${product.shipping_rate}</td>
				<td>{product.tax_rate}</td>
				<td>{product.currency}</td>
				<td>{product.sale}</td>
				<td>{product.sale_percent}</td>
				<td><EditIcon size="24" /></td>
				<td><Trash2Icon size="24" /></td>
			</tr>
		{/each}
	</tbody>
</table>
