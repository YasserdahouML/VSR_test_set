__all__ = [
    "Compose", "Normalize", "CenterCrop"]


class Compose(object):
    """Compose several preprocess together.
    Args:
        preprocess (list of ``Preprocess`` objects): list of preprocess to compose.
    """

    def __init__(self, preprocess):
        self.preprocess = preprocess

    def __call__(self, img):
        for t in self.preprocess:
            img = t(img)
        return img

    def __repr__(self):
        format_string = self.__class__.__name__ + '('
        for t in self.preprocess:
            format_string += '\n'
            format_string += '    {0}'.format(t)
        format_string += '\n)'
        return format_string


class Normalize(object):
    """Normalize a ndarray image with mean and standard deviation.
    """

    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def __call__(self, img):
        """
        Args:
            tensor (Tensor): Tensor image of size (C, H, W) to be normalized.
        Returns:
            Tensor: Normalized Tensor image.
        """
        # try:
        img = (img - self.mean) / self.std
        # except:
        #     pass

        return img

    def __repr__(self):
        return self.__class__.__name__+'(mean={0}, std={1})'.format(self.mean, self.std)



class CenterCrop(object):
    """Crop the given image at the center
    """

    def __init__(self, crop_size):
        self.crop_size = crop_size

    def __call__(self, img):
        """
        Args:
            img (numpy.ndarray): Images to be cropped.
        Returns:
            numpy.ndarray: Cropped image.
        """
        frames, h, w = img.shape
        th, tw = self.crop_size
        delta_w = int(round((w - tw))/2.)
        delta_h = int(round((h - th))/2.)
        return img[:, delta_h:delta_h+th, delta_w:delta_w+tw]

    def __repr__(self):
        return self.__class__.__name__ + '(size={0})'.format(self.crop_size)