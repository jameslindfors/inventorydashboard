// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
// and what to do when importing types
declare namespace App {
	// interface Locals {}
	// interface PageData {}
	// interface Platform {}
	type CollectionType = {
		data: [
			{
				id: number;
				name: string;
				description: string;
				products: [ProductType];
			}
		];
	};
	type ProductType = {
		id: number;
		name: string;
		description: string;
		price: number;
		current_units: number;
		total_units: number;
		shipping_rate: number;
		tax_rate: number;
		currency: string;
		sale: boolean;
		sale_percent: number;
	};
}
