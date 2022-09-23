import { error } from '@sveltejs/kit';

/** @type {import('./$types').PageServerLoad} */
export async function load() {
	const response = await fetch('http://127.0.0.1:8000/inventory/api/c/get-all/collection/');
	if (response.ok) {
		return response.json();
	}

	throw error(404, 'Not found');
}
