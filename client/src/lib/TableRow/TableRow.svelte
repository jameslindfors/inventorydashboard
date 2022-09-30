<script lang="ts">
	import type { ProductType } from '../../types/product.type';
	import Field from '$lib/Field/Field.svelte';
	import { EditIcon, Trash2Icon, CheckSquareIcon, XIcon } from 'svelte-feather-icons';

	export let product: ProductType, editing: boolean;
</script>

<span class="td"><Field name={'name'} value={product.name} {editing} /></span>
<span class="td"><Field name={'price'} value={product.price} {editing} /></span>
<span class="td"><Field name={'current_units'} value={product.current_units} {editing} /></span>
<span class="td"><Field name={'total_units'} value={product.total_units} {editing} /></span>
<span class="td"><Field name={'shipping_rate'} value={product.shipping_rate} {editing} /></span>
<span class="td"><Field name={'tax_rate'} value={product.tax_rate} {editing} /></span>
<span class="td"><Field name={'currency'} value={product.currency} {editing} /></span>
<span class="td"><Field name={'sale'} value={product.sale} {editing} /></span>
<span class="td"><Field name={'sale_percent'} value={product.sale_percent} {editing} /></span>
<span class="td icon is-medium my-2">
	{#if !editing}
		<span
			class="m-1"
			on:click={() => {
				editing = !editing;
			}}
		>
			<EditIcon size="24" />
		</span>
	{:else}
		<button type="submit" formaction="?/update" class="button-override m-1">
			<CheckSquareIcon size="24" class="has-text-success" />
		</button>
	{/if}
</span>
<span class="td icon is-medium my-2">
	{#if !editing}
		<span class="m-2">
			<Trash2Icon size="24" class="has-text-danger" />
		</span>
	{:else}
		<span class="m-3 mx-2" on:click={() => (editing = !editing)}>
			<XIcon size="24" class="has-text-danger" />
		</span>
	{/if}
</span>

<style>
	SPAN.td {
		display: table-cell;
		padding: 0.5em;
	}
	.button-override {
		background-color: white;
		padding: 0;
		margin: 0;
		border: none;
	}
	SPAN.icon {
		vertical-align: middle;
	}
</style>
