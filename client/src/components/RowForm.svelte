<script lang="ts">
	import { EditIcon, Trash2Icon, CheckSquareIcon, XIcon } from 'svelte-feather-icons';
	import Cell from './DataCell.svelte';
	export let product;
	let status = true;
</script>

<tr>
	<Cell cellData={product.name} {status} />
	<Cell cellData={product.price} {status} />
	<Cell cellData={product.current_units} {status} />
	<Cell cellData={product.total_units} {status} />
	<Cell cellData={product.shipping_rate} {status} />
	<Cell cellData={product.tax_rate} {status} />
	<Cell cellData={product.currency} {status} />
	<Cell cellData={product.sale} {status} />
	<Cell cellData={product.sale_percent} {status} />
	<td>
		<span class="icon is-medium my-2">
			{#if status}
				<span on:click={() => (status = !status)}>
					<EditIcon size="24" />
				</span>
			{:else}
				<span>
					<CheckSquareIcon size="24" class="has-text-success" />
				</span>
			{/if}
		</span>
	</td><td>
		<span class="icon is-medium my-2">
			{#if status}
				<span>
					<Trash2Icon size="24" class="has-text-danger" />
				</span>
			{:else}
				<span on:click={() => (status = !status)}>
					<XIcon size="24" class="has-text-danger" />
				</span>
			{/if}
		</span>
	</td>
</tr>
