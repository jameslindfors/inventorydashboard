import type { ProductType } from './product.type';

export type CollectionType = {
	data: [
		{
			id: number;
			name: string;
			description: string;
			products: [ProductType];
		}
	];
};
