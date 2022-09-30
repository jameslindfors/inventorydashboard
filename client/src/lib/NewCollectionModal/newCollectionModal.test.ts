import { render, screen } from '@testing-library/svelte';
import NewCollectionModal from './NewCollectionModal.svelte';

describe('NewCollectionModal', () => {
	test("that the title is 'New Collection'", () => {
		render(NewCollectionModal);
		const title = screen.getByRole('heading');
		expect(title).toHaveTextContent('New Collection');
	});
});
