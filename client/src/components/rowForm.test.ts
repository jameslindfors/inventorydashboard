import { render, screen, fireEvent } from '@testing-library/svelte';
import RowForm from './RowForm.svelte';

describe('RowForm', () => {
	test('that the tr has a td', () => {
		render(RowForm, { props: { product: { name: 'test', price: 1.0, quantity: 1 } } });
		const tr = screen.getByRole('row');
		expect(tr).not.toBeEmptyDOMElement();
	});
});
