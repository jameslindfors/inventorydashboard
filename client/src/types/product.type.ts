export type ProductType = {
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
