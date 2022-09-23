<script>
	import 'bulma/css/bulma.css';
	import { Tabs, Tab } from 'svelma';
	import Table from '/src/components/Table.svelte';

	/** @type {import('./$types').PageData} */
	export let data;

	let tabs = data.data
		.map((/** @type {{ name: any; products: any; }} */ tab) => {
			return {
				label: tab.name,
				component: Table,
				props: {
					products: tab.products
				}
			};
		})
		.slice(0, 5);
</script>

<svelte:head>
	<title>Dashboard</title>
</svelte:head>
<h1 class="mx-4 is-size-2">Inventory Manager</h1>
<br />
<Tabs style="is-boxed">
	{#each tabs as tab}
		<Tab label={tab.label} style="my-0">
			{#if tab.component}
				<svelte:component this={tab.component} {...tab.props} />
			{/if}
		</Tab>
	{/each}
</Tabs>