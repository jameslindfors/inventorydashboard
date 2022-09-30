<script lang="ts">
	import { EditIcon, Trash2Icon, CheckSquareIcon, XIcon } from 'svelte-feather-icons';
	import Cell from '../DataCell/DataCell.svelte';
	import type { ProductType } from '../../types/product.type';

	export let product: ProductType;

	let status = true;
	let formId = product.id + 'form';

	const onSubmit = (e: any) => {
		status = !status;
		let data = new FormData(e.target);
		for (let i = 0; i < e.target.length - 1; ++i) {
			// data = e.target[i].value;
			data.append(e.target[i].name, e.target[i].value);
		}
		console.log(data);
		return data;
	}

</script>

<tr>
	<Cell cellData={product.name} {status} formId={formId} cellType="name"/>
	<Cell cellData={product.price} {status} formId={formId} cellType="price" />
	<Cell cellData={product.current_units} {status} formId={formId} cellType="current_units"/>
	<Cell cellData={product.total_units} {status} formId={formId} cellType="total_units"/>
	<Cell cellData={product.shipping_rate} {status} formId={formId} cellType="shipping_rate"/>
	<Cell cellData={product.tax_rate} {status} formId={formId} cellType="tax_rate"/>
	<Cell cellData={product.currency} {status} formId={formId} cellType="currency"/>
	<Cell cellData={product.sale} {status} formId={formId} cellType="sale"/>
	<Cell cellData={product.sale_percent} {status} formId={formId} cellType="sale_percent"/>
	<td>
		<span class="icon is-medium my-2">
			{#if status}
				<span on:click={() => (status = !status)}>
					<EditIcon size="24" />
				</span>
			{:else}
				<span>
					<form id={formId} on:submit|preventDefault={onSubmit}>
						<button form={formId} type="submit" class="button-overide">
							<CheckSquareIcon size="24" class="has-text-success" />
						</button>
					</form>
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

<style>
	.button-overide {
		background-color: white;
		border: none;
	}
</style>