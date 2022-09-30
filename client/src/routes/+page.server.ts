import type { RequestEvent } from '@sveltejs/kit';
import { error } from '@sveltejs/kit';

/** @type {import('./$types').PageServerLoad} */
export async function load() {
	const response = await fetch('http://127.0.0.1:8000/inventory/api/c/get-all/collection/');
	if (response.ok) {
		return response.json();
	}

	throw error(404, 'Not found');
}

/** @type {import('./$types').Actions} */
export const actions = {
	update: async ({ cookies, request }: RequestEvent) => {
		const data = await request.formData();

		// TODO: validate data

		const body: any = {};
		const id = data.get('product_id');

		data.forEach((value, key) => {
			if (key === 'product_id') {
				return;
			}
			body[key] = value;
		});

		cookies.set('updated_at', Date.now().toLocaleString());

		const response = await fetch(`http://127.0.0.1:8000/inventory/api/p/update/${id}`, {
			method: 'PUT',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(body)
		});

		if (response.ok) {
			return {
				status: 303,
				headers: {
					location: '/'
				}
			};
		}

		return {
			status: 500,
			body: await response.text()
		};
	}
};
